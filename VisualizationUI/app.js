
function fetchData()
{
fetch("http://127.0.0.1:5000/api/stream").then(response => response.json())
    .then(data=>{
        const sentiment = Object.values(data.sentiment)
        const counts = Object.values(data.count)
        updatePieChart(counts)
        
    })
    .catch(error =>{
        console.log(error)
    })
}

function updatePieChart(counts)
{
    const sum = counts.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    function getPercent(count,sum)
    {
        percent = Math.round(count/sum * 100)
        return percent
    }
    const positive = document.getElementById('positive');
    const negative = document.getElementById('negative');
    const neutral = document.getElementById('neutral');


  
    positive.style.setProperty("--p",String(getPercent(counts[1],sum)))
    positive.innerText = String(getPercent(counts[1],sum))+"%"

    negative.style.setProperty("--p",String(getPercent(counts[2],sum)))
    negative.innerText = String(getPercent(counts[2],sum))+"%"

    neutral.style.setProperty("--p",String(getPercent(counts[0],sum)))
    neutral.innerText = String(getPercent(counts[0],sum))+"%"
  

}


fetchData()



function reloadPage() {
    location.reload();
    
}
setInterval(fetchData, 2000);
setInterval(reloadPage, 7000);
 