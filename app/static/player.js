//ADD YOUR CODE HERE.
function gls(data, index) {
    step = data[index]
    if(step) {
        if (step.next == null) {
            div = document.evaluate(step.selector, document.documentElement, null,
                XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null).snapshotItem(0)
        } else {
            div = document.querySelector(step.selector)
        }
        div.innerHTML += gls_view(step.content, step.next-1)
    }
}


function gls_view(content, next) {
    return "<div class='pop-up'>\
                <p>"+content+" <button onclick='changeView("+next+")'>Next</button></p>\
            </div>"    
}

function changeView(next) {
    document.querySelector('.pop-up').remove()
    gls(data, next)    
}