document.querySelector("#loading").innerHTML = "";

const allAddDeckmarkButtons = document.querySelectorAll(".add-deckmark")

for (let i = 0; i < allAddDeckmarkButtons.length; i++) {
    allAddDeckmarkButtons[i].addEventListener('click', (evt) => {
        const targetButton = evt.target;
        const targetId = targetButton.attributes.id.nodeValue.split('-')[2];

        const formInputs = {
            group_id: document.querySelector("#group-select-" + targetId).value,
            link: document.querySelector("#ss-url-" + targetId).href, 
            description: document.querySelector("#ss-description-" + targetId).innerText, 
            thumbnail: document.querySelector("#ss-thumbnail-" + targetId).src, 
        }

        fetch('/create_deckmark_json', {
            method: 'POST', 
            body: JSON.stringify(formInputs), 
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then( response => console.log(response));
    });

}