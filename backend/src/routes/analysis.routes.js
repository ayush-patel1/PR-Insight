const express = require("express")
const router = express.Router()
const analysisController = require("../controllers/analysis.controller")
const authMiddleware = require("../middleware/auth.middleware")

router.post("/request", authMiddleware, analysisController.requestAnalysis)

module.exports = router
