import Head from 'next/head'
import dynamic from 'next/dynamic'

import fetch from 'isomorphic-unfetch'

const Device = dynamic(() => import('../components/device'))

const config = require('../config')

import "../styles/main.scss"

export default class extends React.Component {
  static async getInitialProps({ req }) {
    const url = req ? `http://localhost:${config.server.port}/api/devices` : '/api/devices'
    const res = await fetch(url)
    const { data: devices } = await res.json()

    return { devices }
  }

  render () {
    const { devices } = this.props

    return (
      <div>
        <Head>
            <meta charSet="utf-8" />
            <meta httpEquiv="X-UA-Compatible" content="IE=edge,chrome=1" />
            <title>KWHC UI</title>
            <meta name="description" content="" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />

            <link rel="apple-touch-icon-precomposed" sizes="57x57" href="/static/img/icons/apple-touch-icon-57x57.png" />
            <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/img/icons/apple-touch-icon-114x114.png" />
            <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/img/icons/apple-touch-icon-72x72.png" />
            <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/img/icons/apple-touch-icon-144x144.png" />
            <link rel="apple-touch-icon-precomposed" sizes="120x120" href="/static/img/icons/apple-touch-icon-120x120.png" />
            <link rel="apple-touch-icon-precomposed" sizes="152x152" href="/static/img/icons/apple-touch-icon-152x152.png" />
            <link rel="icon" type="image/png" href="/static/img/icons/favicon-32x32.png" sizes="32x32" />
            <link rel="icon" type="image/png" href="/static/img/icons/favicon-16x16.png" sizes="16x16" />
            <meta name="application-name" content="KWHC"/>
            <meta name="msapplication-TileColor" content="#FFFFFF" />
            <meta name="msapplication-TileImage" content="/static/img/icons/mstile-144x144.png" />
        </Head>

        {devices.map((device, index) =>
          <Device
            key={`device-${index}`}
            index={index}
            name={device.name} />
        )}
      </div>
    )
  }
}
