document.getElementById('food-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const foodName = document.getElementById('food-name').value;
    const portion = document.getElementById('portion').value;

    const response = await fetch('http://127.0.0.1:5000/add-food', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ foodName, portion }),
    });

    const data = await response.json();
    document.getElementById('calorie-log').innerText = `Total Calories: ${data.totalCalories}`;
});
