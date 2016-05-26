$(document).ready(function() 
{
    var hei = $("#editor").parent("#editor-container").parent().height();
    $("#editor").parent("#editor-container").css({ "height": hei + 'px' });
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.getSession().setMode("ace/mode/latex");
    $('#editor').css("fontSize", "16px");
    $("#editor").resizable();
    editor.setOptions({
        enableBasicAutocompletion: true,
        enableSnippets: true,
        enableLiveAutocompletion: true
    });

    var doc = editor.getSession().getDocument();
    $("#editor").css({ "height": hei + 'px' });
    editor.resize();
    $('#pdf-container').resizable();
    $('#pdf-viewport').resizable();
    $("#pdf-container").css({ "height": hei + 'px' });

    // var ws = new WebSocket(); TODO
    editor.on('change', function(e){
        console.dir(e);
    });
});
