/**
 * Created by Administrator on 2016/9/27.
 */
tinymce.init({
    selector: 'textarea',
    height: 300,
    // language: 'zh_CN',
    plugins: [
        'codesample advlist autolink link image imagetools lists charmap print preview hr anchor pagebreak spellchecker',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'save table contextmenu directionality emoticons template paste textcolor'
    ],
    toolbar: 'insertfile undo redo | fontsizeselect fontselect forecolor backcolor emoticons| bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media | codesample removeformat ',
    fontsize_formats: '8pt 10pt 12pt 14pt 18pt 24pt 36pt',
    // font_formats: 'Arial=arial,helvetica,sans-serif;Courier New=courier new,courier,monospace;AkrutiKndPadmini=Akpdmi-n,aileron',
    code_dialog_height: 200,
    imagetools_toolbar: "rotateleft rotateright | flipv fliph | editimage imageoptions",
    content_css: [
    '//fast.fonts.net/cssapi/e6dc9b99-64fe-4292-ad98-6974f93cd2a2.css',
    '//www.tinymce.com/css/codepen.min.css'
    ]
});
