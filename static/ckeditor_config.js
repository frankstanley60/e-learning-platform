// ckeditor_config.js
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

ClassicEditor
    .create(document.querySelector('#editor'), {
        plugins: [ 'MathType' ],
        toolbar: [ 'MathType', '|' ]
    })
    .catch(error => {
        console.error(error);
    });
