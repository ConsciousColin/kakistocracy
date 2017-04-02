/*
function building_one( this ) {
        if (this == 'letter') {
                return ''
            }
        }

$("#comic_sans").click(change_font())

function change_font () {
        var idee = document.getElementById("comic_sans")
        $("#comic_sans").click( 
                $(".post").style.fontfamily == "Comic Sans MS"
                )
        }
        $(".post").css("font-family",  "Comic Sans MS");
*/

$(document).ready(function(){
    $("button").click(function(){
         $(".post").toggleClass("cs_post")
    });
});

