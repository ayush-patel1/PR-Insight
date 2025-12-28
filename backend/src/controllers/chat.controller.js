const Message = require("../models/Message")

// Get all messages
exports.getMessages = async (req, res) => {
  try {
    const messages = await Message.find().populate("user", "username").sort({ timestamp: 1 }).limit(100)

    res.json({ messages })
  } catch (error) {
    console.error("Get messages error:", error)
    res.status(500).json({ message: "Server error" })
  }
}

// Save a message
exports.saveMessage = async (req, res) => {
  try {
    const { content } = req.body
    const userId = req.user.id

    const message = new Message({
      user: userId,
      username: req.user.username,
      content,
    })

    await message.save()

    res.status(201).json({ message: "Message saved", data: message })
  } catch (error) {
    console.error("Save message error:", error)
    res.status(500).json({ message: "Server error" })
  }
}
