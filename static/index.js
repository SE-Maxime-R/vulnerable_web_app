
function check_creds() {
    const username = document.getElementById('user').value;
    const password = document.getElementById('passwd').value;

    const real_user = atob("YWRtaW4=")
    const real_pass = atob("cm9vdA==")
    
    console.log(`Username: ${username}`);
    console.log(`Password: ${password}`);

    if (username == real_user && password == real_pass) {
        window.location.replace('admin.html');
    } else if (username == 'user' && password == 'noob') {
        window.location.replace('greetings.html');
    } else {
        throw new Error('Invalid credentials');
    }
    
}

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('xssForm');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent reload
        const message = document.getElementById('mess').value;
        document.getElementById('response').style.display = "block";
        document.getElementById('response').innerHTML = "Your message said: " + message;
    });
});