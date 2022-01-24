function display_tags(deckmark_id){
    fetch(`/deckmark/${deckmark_id}/tags`)
        .then( response => response.json())
        .then( responseData => {
            const tags = responseData.tags; 
            document.querySelector(`#tags-${deckmark_id}`).innerHTML = responseData.tags;
        })
}

allAddButtons = document.querySelectorAll(".add-button");

for (let i = 0; i < allAddButtons.length; i++) {
    allAddButtons[i].addEventListener('click', (evt) => {
        const targetButton = evt.target;
        const targetId = String(targetButton.attributes.id.nodeValue.split('-')[2])
        const tagHTMLID = `#tags-${targetId}`
        const newTag = document.querySelector(`#tag-input-${targetId}`).value;

        fetch('/api/create_tag', {
                method: 'POST', 
                body: JSON.stringify({ name: newTag}), 
                headers: { 'Content-Type': 'application/json'},
                })
            .then( response => response.json())
            .then( responseData => {
                const tagID = responseData.tag_id

                const formInputs = {
                    deckmark_id: targetId,
                    tag_id: tagID
                }

                fetch('/api/add_tag_to_deckmark', {
                    method: 'POST', 
                    body: JSON.stringify(formInputs), 
                    headers: {'Content-Type': 'application/json'},
                    })
                .then( response => {
                    display_tags(targetId);
                    }
                );
            });
    });

}