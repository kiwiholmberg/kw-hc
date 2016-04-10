

var KWHC = {
    init: function() {
        // Bind device buttons
        $('.device__button').on('click', this.controlDevice)
    },
    controlDevice: function(e) {
        var action = $(e.currentTarget).data('action')
        var name = $(e.currentTarget).parent('.device').data('name')

        var url = window.baseUrl
                  + 'control/device/'
                  + encodeURIComponent(name) + '/'
                  + encodeURIComponent(action)
        $.post(url, function(data) {
            console.log(data)
        })
    }
}

window.baseUrl = ''
window._wkhc = KWHC
window._wkhc.init()
