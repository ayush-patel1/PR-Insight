const Message = require("../models/Message")
const axios = require("axios")

exports.requestAnalysis = async (req, res) => {
  try {
    // Fetch recent messages
    const messages = await Message.find().sort({ timestamp: -1 }).limit(50).select("username content timestamp")

    if (messages.length === 0) {
      return res.status(400).json({ message: "No messages to analyze" })
    }

    // Format messages for AI service
    const formattedMessages = messages.reverse().map((msg) => ({
      username: msg.username,
      content: msg.content,
      timestamp: msg.timestamp,
    }))

    // Call Python AI service
    const aiServiceUrl = process.env.AI_SERVICE_URL || "http://localhost:8000"
    const response = await axios.post(`${aiServiceUrl}/analyze`, {
      messages: formattedMessages,
    })

    res.json({
      message: "Analysis completed",
      analysis: response.data,
    })
  } catch (error) {
    console.error("Analysis error:", error)
    res.status(500).json({ message: "Failed to generate analysis" })
  }
}
