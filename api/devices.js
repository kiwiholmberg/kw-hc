const pify = require('pify')
const telldus = pify(require('telldus'))

async function list (req, res) {
  const data = await telldus.getDevices()
  return res.json({ data })
}

async function control (req, res) {
  const { name, command } = req.params
  const devices = await telldus.getDevices()

  const device = devices.find(device => device.name === name)

  if (!device) return res.status(404)

  console.log(`Set device ${device.name} status to ${command}`)
  try {
    if (command === 'on') {
      await telldus.turnOn(device.id)
    } else if (command === 'off') {
      await telldus.turnOff(device.id)
    } else {
      return res.status(400).json({ status: 'Invalid command (valid: on|off)' })
    }
  } catch (err) {
    console.log(err)
    if (err.name === 'TelldusError') return res.status(503).json({ status: 'Radio interface error' })
    return res.status(503).json({ status: 'Unknown error' })
  }

  return res.json({ status: 'ok' })
}

module.exports = { list, control }
