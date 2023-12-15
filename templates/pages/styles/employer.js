const listedJobs = [
    {
      title: 'Software Engineer',
      salary: '$80,000',
      location: 'City A',
      description: 'Exciting software development opportunity',
      status: 'pending' // 'pending', 'accepted', 'declined', or other statuses
    },
    {
      title: 'Data Analyst',
      salary: '$60,000',
      location: 'City B',
      description: 'Analyzing and interpreting complex data sets',
      status: 'accepted'
    },
    // Add more jobs as needed
  ];

  function listJob() {
    const jobTitle = document.getElementById('jobTitle').value;
    const salary = document.getElementById('salary').value;
    const location = document.getElementById('location').value;
    const description = document.getElementById('jobDescription').value;
  
    const job = { title: jobTitle, salary, location, description, status: 'pending' };
    listedJobs.push(job);
  
    displayListedJobs();
  }
  
  function displayListedJobs() {
    const listedJobsContainer = document.querySelector('.listed-jobs ul');
    listedJobsContainer.innerHTML = '<h2>Listed Jobs</h2>';
  
    if (listedJobs.length === 0) {
      listedJobsContainer.innerHTML += '<p>No jobs listed yet.</p>';
      return;
    }
  
    listedJobs.forEach((job, index) => {
      const li = document.createElement('li');
      li.textContent = `${job.title} - ${job.location} - ${job.salary}`;
      
      const acceptButton = document.createElement('button');
      acceptButton.textContent = 'Accept';
      acceptButton.addEventListener('click', () => acceptJob(index));
      
      const declineButton = document.createElement('button');
      declineButton.textContent = 'Decline';
      declineButton.addEventListener('click', () => declineJob(index));
  
      li.appendChild(acceptButton);
      li.appendChild(declineButton);
  
      listedJobsContainer.appendChild(li);
    });
  }
  
  function acceptJob(index) {
    listedJobs[index].status = 'accepted';
    displayListedJobs();
    // You may want to handle additional logic here, e.g., notify the job seeker
  }
  
  function declineJob(index) {
    listedJobs[index].status = 'declined';
    displayListedJobs();
    // You may want to handle additional logic here, e.g., notify the job seeker
  }