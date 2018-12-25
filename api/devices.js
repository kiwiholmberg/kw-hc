const mockDevices = [{
    id: 1,
    name: 'Table lamp',
    methods: [ 'TURNON', 'TURNOFF' ],
    model: 'codeswitch',
    type: 'DEVICE',
    status: {status: 'OFF'}
}, {
    id: 2,
    name: 'Spotlights',
    methods: [ 'TURNON', 'TURNOFF' ],
    model: 'codeswitch',
    type: 'DEVICE',
    status: {status: 'OFF'}
}, {
    id: 3,
    name: 'Downlights',
    methods: [ 'TURNON', 'TURNOFF' ],
    model: 'codeswitch',
    type: 'DEVICE',
    status: {status: 'OFF'}
}]

function get (req, res) {
    return res.json({ data: mockDevices})
}

module.exports = { get }
