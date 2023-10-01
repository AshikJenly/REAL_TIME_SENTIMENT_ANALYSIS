// Function to fetch data from the API and populate the table
function populateTable() {
    const tableBody = document.getElementById('tweetCardContainer');

    fetch('http://localhost:5000/api/getalltweets')
        .then((response) => response.json())
        .then((data) => {
            // Loop through the fetched data and populate the table
            for (let i = 0; i < Object.keys(data.tweet_id).length; i++) {

                const tweetCard = document.createElement('div');
                tweetCard.className = 'card tweet-card';
                tweetCard.innerHTML = `
                    <div class="card-body">
                        <h5 class="card-title">${data.username[i]}</h5>
                        <p class="card-text">${data.tweet_data[i]}</p>
                        
                    </div>
                `;

                tableBody.appendChild(tweetCard);
            }
        })
        .catch((error) => {
            console.error('Error fetching data:', error);
        });
}

// ----------------  Menu Bar module --------------------
function menuBarShow()
{
    if (!isShowing)
    {
        const menu_contents = document.getElementById('cont-1-id');
        csstext = `
            display:block;
            background-color:  #fbfaf8;
            z-index:100;
            height:100vh;
        `
        
        menu_contents.style.cssText = csstext
        isShowing = true
    }
    else{
        isShowing = false

        const svgElement = document.getElementById('menu-svg');
        svgElement.querySelector('image').setAttribute('xlink:href', 'https://www.svgrepo.com/show/521564/close.svg');
    }

}

const button = document.getElementById('menu-b');
button.onclick = menuBarShow

let isShowing = false
// -------------------------------------------------------------
function handleScreenWidthChange()
{
    
    const screenWidth = window.innerWidth;

    if (screenWidth > 1200) {
        location.reload()
        console.log('Screen width is less than 768 pixels.');
    } else if(screenWidth < 500){
        location.reload()
        console.log('Screen width is 768 pixels or more.');
    }
}

// Call the function to populate the table when the page loads
window.onload = populateTable;
window.addEventListener('resize', handleScreenWidthChange);
