require("dotenv").config()
const http = require("http")
const app = require("./app")
const connectDB = require("./config/db")
const initializeSocket = require("./socket/socket")

const PORT = process.env.PORT || 5000

// Connect to database
connectDB()

// Create HTTP server
const server = http.createServer(app)

// Initialize Socket.io
initializeSocket(server)

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})
