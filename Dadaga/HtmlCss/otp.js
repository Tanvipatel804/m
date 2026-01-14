function moveFocus(currentInput) {
    if (currentInput < 6) {
        document.getElementById('otp' + (currentInput + 1)).focus();
    }
}

function verifyOTP() {
    const otp = [
        document.getElementById('otp1').value,
        document.getElementById('otp2').value,
        document.getElementById('otp3').value,
        document.getElementById('otp4').value,
        document.getElementById('otp5').value,
        document.getElementById('otp6').value,
    ];

    const enteredOTP = otp.join('');
    const correctOTP = '123456';  // Example OTP for testing

    if (enteredOTP === correctOTP) {
        document.getElementById('message').textContent = 'OTP Verified Successfully!';
        document.getElementById('message').style.color = 'green';
    } else {
        document.getElementById('message').textContent = 'Invalid OTP, please try again.';
        document.getElementById('message').style.color = 'red';
    }
}
