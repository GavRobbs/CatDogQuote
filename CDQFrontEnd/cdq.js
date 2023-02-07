function ask_api()
{
    document.getElementById('loading-text').style.display = 'block';

    fetch('https://7t2uz5sxjc.execute-api.us-east-1.amazonaws.com/PerpetualBeta/test')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });

    fetch('https://7t2uz5sxjc.execute-api.us-east-1.amazonaws.com/PerpetualBeta/inspire')
    .then(response => response.json())
    .then(data => {
        populate_document(data)
        document.getElementById('loading-text').style.display = 'none';
    });
}

function populate_document(data)
{
    document.getElementById('text-content').innerText = data.quote;
    document.getElementById('catpic_img').src = data.cat_pic;
    document.getElementById('dogpic_img').src = data.dog_pic;

}

ask_api();