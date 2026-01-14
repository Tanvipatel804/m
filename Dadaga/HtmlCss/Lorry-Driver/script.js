function goBack() {
      window.history.back();
    }
document.addEventListener('DOMContentLoaded', () => {
    const contentDiv = document.getElementById('content');
    const links = document.querySelectorAll('.nav-item');

    // Function to load content based on the page name
    function loadPage(pageName) {
        let htmlContent = '';
        switch (pageName) {
            case 'status':
                htmlContent = `
                    <div class="page-container">
                        <h2>Status</h2>
                        <div class="status-grid">
                            <div class="card" style="background-color: #5d6afe; color: white;">
                                <p>Pool member number</p>
                                <h2>128</h2>
                                  <span class="icon">🚚</span>
                            </div>
                            <div class="card">
                                <p>Number of pool ride completion</p>
                                <h2>2,456</h2>
                                  <span class="icon">🚚</span>
                            </div>
                            <div class="card" style="background-color: #5d6afe; color: white;">
                                <p>Time saving</p>
                                <h2>350 hrs</h2>
                                 <span class="icon">&#128337;</span>
                            </div>
                            <div class="card" style="background-color: #4CAF50; color: white;">
                                <p>CO2 protector</p>
                                <h2>850 kg saved</h2>the world from emissions
                                <span class="icon">&#127807;</span>
                            </div>
                            <div class="card card-large">
                                <p>Total pool income generate</p>
                                <h2>$12,345</h2>
                                  <span class="icon">&#127870;</span>
                            </div>
                        </div>
                    </div>
                `;
                break;
            case 'membership':
                htmlContent = `
                    <div class="page-container">
                        <h2>Membership</h2>
                        <div class="toggle-switch">
                            <p>Apply for pool membership campaign</p>
                            <input type="checkbox" id="toggle-switch" class="toggle-switch-input" checked>
                            <label for="toggle-switch" class="toggle-switch-label"></label>
                        </div>
                        <div class="benefits">
                            <h3>Benefits</h3>
                            <ul>
                                <li>Access to all pool facilities</li>
                                <li>Discount on swimming lessons</li>
                                <li>Priority booking for events</li>
                            </ul>
                            <button class="btn btn-green">Accept</button>
                        </div>
                        <div class="policy">
                            <h3>Policy</h3>
                            <div class="policy-text">
                                <p>Wares to all pool facilities, membersing on the Membership eopwuset for eaking and all abes, par boents</p>
                                <p>Secblle cerdcks fiorest the policy sur cereis of the terms all conditions</p>
                            </div>
                            <button class="btn btn-black">Accept</button>
                            <button class="btn btn-black" style="margin-top: 10px;">Submit</button>
                        </div>
                    </div>
                `;
                break;
            case 'rides':
                htmlContent = `
                    <div class="page-container">
                        <h2>Ride Detail</h2>
                        <div class="ride-detail">
                            <div class="map-placeholder">
                              <img src="C:/Users/DADAGA/Pictures/Saved Pictures/locationshow.jpg" alt="Material">
                            </div>
                            <div class="address-info">
                                <span>Loading from address</span>
                                <span>Destination address</span>
                            </div>
                            <div class="ride-details-card">
                                <div class="ride-image">
                                    <img src="C:/Users/DADAGA/Pictures/Saved Pictures/cement.jpg" alt="Material">
                                </div>
                                <div class="ride-details-text">
                                    <p>Traveling Range: 150 km</p>
                                    <p>Earned: $75.00</p>
                                    <p>Date/Time: 12/05/2024, 10:30 AM</p>
                                    <p>Duration: 2 hours 15 mins</p>
                                </div>
                            </div>
                            <button class="btn btn-black" style="margin-top: 20px;">Confirm Ride</button>
                        </div>
                    </div>
                `;
                break;
        }
        contentDiv.innerHTML = htmlContent;
    }

    // Handle navigation clicks
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            links.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            const pageName = link.id.split('-')[0];
            loadPage(pageName);
        });
    });

    // Load the initial page (Status)
    loadPage('status');
});