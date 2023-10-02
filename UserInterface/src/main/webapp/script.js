// Function to fetch data from the API and populate the table
function populateTable() {
    const tableBody = document.getElementById('tweetCardContainer');

    fetch('http://localhost:5000/api/getalltweets')
        .then((response) => response.json())
        .then((data) => {
            // Loop through the fetched data and populate the table
            for (let i = 0; i < Object.keys(data.tweet_id).length; i++) {

                const tweetCard = document.createElement('div');
                tweetCard.className = '';
                tweetCard.innerHTML = `
                    <div class="">
                <ul class="tweet-user-list">
                    <div>
                    <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="cont-1-fc">
                        <image xlink:href="https://www.svgrepo.com/show/532363/user-alt-1.svg" width="24" height="24"/>
                    </svg>
                    </div>
                        <h5 class="user-name">${data.username[i]}</h5>
                        <h5 class="user-id">${data.tweet_id[i]}</h5>
                        </div>
                        </ul>
                        <p class="tweet-data">${data.tweet_data[i]}</p> 
                        <image class="tweet-image" src="https://imgs.search.brave.com/emP17o4aBNSQyp-I34fjtKsE8-7wX77REodmB_o34Aw/rs:fit:860:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy83/Lzc5L1RoZV9TcGFj/ZVhfRmFjdG9yeS5q/cGc" rel="sampleimage" >  
                <ul class="impression-list">
                <li>
                    <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="cont-1-fc">
                    <image xlink:href="https://www.svgrepo.com/show/533232/message-circle.svg" width="24" height="24"/>
                    </svg>
                    <p>23k</p>
                </li>
                <li>
                    <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="cont-1-fc">
                    <image xlink:href="https://www.svgrepo.com/show/349614/retweet.svg" width="24" height="24"/>
                    </svg>
                    <p>12.4k</p>
                </li>
                <li>
                    <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="cont-1-fc">
                    <image xlink:href="https://www.svgrepo.com/show/524063/heart.svg" width="24" height="24"/>
                    </svg>
                    <p>19.1k</p>
                </li>
                <li>
                    <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="cont-1-fc">
                    <image xlink:href="https://www.svgrepo.com/show/471048/bar-chart-04.svg" width="24" height="24"/>
                    </svg>
                    <p>23k</p>
                </li>
                <li>
                    <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" class="cont-1-fc">
                    <image xlink:href="https://www.svgrepo.com/show/511124/share-ios-export.svg" width="24" height="24"/>
                    </svg>
                </li>
                </ul>
                <hr>
                
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
    if (isShowing == false)
    {
        const menu_contents = document.getElementById('cont-1-id');
        csstext = `
            display:block;
            background-color:  #fbfaf8;
            z-index:100;
            height:100vh;
        `
        const svgLogo = document.getElementById('logo-home-id');
        const svgElement = document.getElementById('menu-svg');
        svgLogo.style.cssText = `display:none`
        svgElement.querySelector('image').setAttribute('xlink:href', 'https://www.svgrepo.com/show/521564/close.svg');
       
        menu_contents.style.cssText = csstext
        isShowing = true
    }
    else{
        isShowing = false
        const menu_contents = document.getElementById('cont-1-id');
        csstext = `
            display:none;
            background-color:  #fbfaf8;
            z-index:100;
            height:100vh;
        `
        menu_contents.style.cssText = csstext
        const svgLogo = document.getElementById('logo-home-id');
        const svgElement = document.getElementById('menu-svg');
        
        svgLogo.style.cssText = `display:block`
        svgElement.querySelector('image').setAttribute('xlink:href', 'https://www.svgrepo.com/show/532195/menu.svg');
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
