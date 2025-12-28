const express = require("express")
const cors = require("cors")
const authRoutes = require("./routes/auth.routes")
const chatRoutes = require("./routes/chat.routes")
const analysisRoutes = require("./routes/analysis.routes")

const app = express()

// Middleware
app.use(
  cors({
    origin: process.env.FRONTEND_URL || "http://localhost:3000",
    credentials: true,
  }),
)
app.use(express.json())

// Routes
app.use("/api/auth", authRoutes)
app.use("/api/chat", chatRoutes)
app.use("/api/analysis", analysisRoutes)

// Health check
app.get("/health", (req, res) => {
  res.json({ status: "ok" })
})

module.exports = app
