import React from 'react'
import fetch from 'isomorphic-unfetch'

export default class extends React.Component {
  async sendControlRequest (name, command) {
    return fetch(`/api/devices/${encodeURIComponent(name)}/${encodeURIComponent(command)}`, { method: 'POST' })
  }

  render () {
    const { name, index } = this.props
    const indexClassName = `bg-color--${index % 5}`

    return (
      <div className={`device ${indexClassName}`}>
        <h1 className='device__title'>{name}</h1>
        <button
          className='device__button device__button--on'
          onClick={() => this.sendControlRequest(name, 'on')}>On</button>

        <button
          className='device__button device__button--off'
          onClick={() => this.sendControlRequest(name, 'off')}>Off</button>
      </div>
    )
  }
}
