/**
 * Created by Administrator on 2016/9/27.
 */
tinymce.init({
    selector: 'textarea',
    height: 300,
    plugins: [
        'codesample advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'save table contextmenu directionality emoticons template paste textcolor'
    ],
    toolbar: 'insertfile undo redo | fontsizeselect | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media fullpage | forecolor backcolor emoticons codesample removeformat ',
    fontsize_formats: '8pt 10pt 12pt 14pt 18pt 24pt 36pt',
    font_formats: 'Arial=arial,helvetica,sans-serif;Courier New=courier new,courier,monospace;AkrutiKndPadmini=Akpdmi-n',
    code_dialog_height: 200
});