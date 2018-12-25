const express = require('express')
const devices = require('./api/devices')

const app = express()

app.get('/api/health', (req, res) => { res.send('Hello World') })

app.get('/api/devices', devices.get)

app.use(express.static('public'))

app.listen(3000)
