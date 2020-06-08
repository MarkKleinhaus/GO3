// CODE FOR SELECTING SECTIONS
function section_select(objecttype, objectid, item, sectionid, sectionname, csrf_token) {
    $.ajax({
        method: 'POST',
        url: '/'+objecttype+'/'+objectid+'/section/'+sectionid,
        headers: { "X-CSRFToken": csrf_token },
        success: function(responseTxt,statusTxt,xhr){
                    if(statusTxt=="success")
                        setTimeout(function(){document.getElementById(item).innerHTML=sectionname}, 1000);
                    if(statusTxt=="error")
                        alert("Error: "+xhr.status+": "+xhr.statusText);
                },
    });
}




// CODE FOR COMMENTS ON AGENDA PAGE
function show_comment(the_plan) {
    $('#comment-init-'+the_plan).hide();
    $('#comment-row-'+the_plan).show();
    setTimeout(function(){
        $('#comment-'+the_plan).click();
    }, 100);
}

function closed_comment(thing) {
    if ($('#comment-'+thing).text()=='') {
        $('#comment-init-'+thing).show();
        $('#comment-row-'+thing).hide();
    }
}

function init_plan_comments(token) {
    $('.comment-thing').editable({
        emptytext: '<i class="far fa-comment"></i>',
        emptyclass: 'empty-comment',
        mode: 'inline',
        ajaxOptions: { headers: {"X-CSRFToken": token }},
    }).on('hidden', function(e, reason) {
        closed_comment(e.target.getAttribute('data-pk'));
    })
    
}

$(document).ready(function() {
});

