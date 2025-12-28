const socketIO = require("socket.io")
const jwt = require("jsonwebtoken")
const Message = require("../models/Message")

const initializeSocket = (server) => {
  const io = socketIO(server, {
    cors: {
      origin: process.env.FRONTEND_URL || "http://localhost:3000",
      methods: ["GET", "POST"],
    },
  })

  // Socket authentication middleware
  io.use((socket, next) => {
    const token = socket.handshake.auth.token

    if (!token) {
      return next(new Error("Authentication error"))
    }

    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET)
      socket.user = decoded
      next()
    } catch (error) {
      next(new Error("Authentication error"))
    }
  })

  io.on("connection", (socket) => {
    console.log("User connected:", socket.user.username)

    // Join room
    socket.join("discussion-room")

    // Handle new message
    socket.on("send-message", async (data) => {
      try {
        const message = new Message({
          user: socket.user.id,
          username: socket.user.username,
          content: data.content,
        })

        await message.save()

        // Broadcast to all users in room
        io.to("discussion-room").emit("new-message", {
          id: message._id,
          username: message.username,
          content: message.content,
          timestamp: message.timestamp,
        })
      } catch (error) {
        console.error("Error saving message:", error)
      }
    })

    socket.on("disconnect", () => {
      console.log("User disconnected:", socket.user.username)
    })
  })

  return io
}

module.exports = initializeSocket
