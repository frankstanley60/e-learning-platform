// ckeditorConfig.js

import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import MathEquationPlugin from './plugins/mathEquation/mathEquationPlugin';

ClassicEditor
    .create(document.querySelector('#lesson_content'), {
        plugins: [MathEquationPlugin],
        toolbar: {
            items: [
                'heading',
                '|',
                'bold',
                'italic',
                'link',
                'bulletedList',
                'numberedList',
                '|',
                'mathEquationPlugin', // Add the math equations button here
                '|',
                'undo',
                'redo'
            ]
        },
        language: 'en',
        // Add any other configuration options here
    })
    .then(editor => {
        console.log('CKEditor initialized with Math Equation plugin.');
    })
    .catch(error => {
        console.error(error.stack);
    });
