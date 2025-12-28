const express = require("express")
const router = express.Router()
const chatController = require("../controllers/chat.controller")
const authMiddleware = require("../middleware/auth.middleware")

router.get("/messages", authMiddleware, chatController.getMessages)
router.post("/message", authMiddleware, chatController.saveMessage)

module.exports = router
