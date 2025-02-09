document.addEventListener('DOMContentLoaded', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs && tabs[0]) {
      const activeTab = tabs[0];
      const videoUrl = activeTab.url;

      // Add click event listener to the download button
      document.getElementById('downloadBtn').addEventListener('click', async () => {
        const status = document.getElementById('status');
        status.textContent = 'Processing...';

        try {
          // Replace with your actual server URL if needed
          const response = await fetch('http://localhost:5000/download_audio', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: videoUrl })
          });
          
          const data = await response.json();
          if (response.ok) {
            status.textContent = data.message;
          } else {
            status.textContent = 'Error: ' + data.error;
          }
        } catch (err) {
          status.textContent = 'Fetch error: ' + err.message;
        }
      });
    } else {
      document.getElementById('videoTitle').textContent = 'No active tab found.';
    }
  });
});
