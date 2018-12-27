const express = require('express')
require('express-async-errors')

const next = require('next')

const config = require('./config')
const devices = require('./api/devices')

const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  const server = express()

  // API rutes
  server.get('/api/devices', devices.list)
  server.post('/api/devices/:name/:command', devices.control)

  // Page routes
  server.get('*', (req, res) => handle(req, res))

  server.listen(config.server.port)
  console.log(`Listening on port ${config.server.port}`)
})
.catch((ex) => {
  console.error(ex.stack)
  process.exit(1)
})
