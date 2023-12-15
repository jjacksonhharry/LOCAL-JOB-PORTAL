// Assume you have an array of jobs (for demonstration purposes)
const jobs = [
    { title: 'Software Engineer', location: 'City A', type: 'Full-time' },
    { title: 'Data Analyst', location: 'City B', type: 'Part-time' },
    // Add more job objects as needed
  ];
  
  function searchJobs() {
    const keyword = document.getElementById('keyword').value.toLowerCase();
    const jobType = document.getElementById('jobType').value.toLowerCase();
    const location = document.getElementById('location').value.toLowerCase();
  
    const filteredJobs = jobs.filter(job =>
      job.title.toLowerCase().includes(keyword) &&
      job.type.toLowerCase().includes(jobType) &&
      job.location.toLowerCase().includes(location)
    );
  
    displayJobs(filteredJobs);
  }
  
  function displayJobs(jobs) {
    const jobResultContainer = document.querySelector('.jobResultContainer');
    jobResultContainer.innerHTML = '<h1>Job Results</h1>';
  
    if (jobs.length === 0) {
      jobResultContainer.innerHTML += '<p>No matching jobs found.</p>';
      return;
    }
  
    const ul = document.createElement('ul');
    jobs.forEach(job => {
      const li = document.createElement('li');
      li.textContent = `${job.title} - ${job.location} - ${job.type}`;
      ul.appendChild(li);
    });
  
    jobResultContainer.appendChild(ul);
  }
  
  function applyForJob() {
    // Logic for handling job application goes here
    alert('Job application submitted!');
  }
  