const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const alertBox = document.getElementById('alert-box')

const handleAlerts = (type, msg) =>{
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
        ${msg}
    </div>`
}

Dropzone.autoDiscover = false
const myDropzone = new Dropzone('#my-dropzone', {
    url: '/reports/upload-json/',
    init: function() {
        this.on('sending', function(file, xhr, formData){
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('success', function(file, response){
            console.log(response.ex)
            const ex = response.ex
            if(ex) {
                handleAlerts('danger', 'Файл уже существует')
            } else {
                handleAlerts('success', 'Ваш файл загружен')
            }
        })
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: '.json'
})