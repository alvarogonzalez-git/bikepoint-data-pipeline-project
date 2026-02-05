<div align="center">
  <p>
    <img width="38%" alt="tfl logo" src="https://github.com/user-attachments/assets/4a711b29-8347-4f2f-bbfc-27a0f3932192" />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img width="38%" alt="santander cycles logo" src="https://github.com/user-attachments/assets/564ded8a-68db-4b26-989d-97b9882f1fab" />
  </p>

  <h1>TfL BikePoint Data Pipeline</h1>

  <p>
    A robust <strong>ELT pipeline</strong> ingesting data from <a href="https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_Get">Transport for London's (TfL) BikePoint API</a> and loading to <strong>AWS S3</strong>. This data is warehoused in <strong>Snowflake</strong> and <strong>dbt Platform</strong> is used to transform and model the warehoused data to make it analysis-ready.
  </p>
</div>

<hr />

<h2>🚀 Project Architecture</h2>

<p>The pipeline consists of three stages:</p>
<ol>
  <li><strong>Extract & Load with Python 🐍 </strong>
  <ul>
    <li><code>main.py</code> - This python script orchestrates the extract & load process. It manages the runtime environment, environment variables, and triggers the sequence of events.</li>
    <li><code>extract.py</code> - this python module script connects to the TfL API, handles connectivity errors with retries, and saves raw data locally.</li>
    <li><code>load.py</code> -  this python module script checks for local data, authenticates with AWS, uploads files to an S3 bucket, and cleans up local storage upon success.</li>
  </ul>

  <li><strong>Warehousing - Snowflake ❄️</strong>
  <ul>
    <li><i>Coming soon - loading to Snowflake...</i></li>
  </ul>
  <li><strong>Transform with dbt Plaform 🔶</strong>
  <ul>
    <li><i>Coming soon - transformation with dbt...</i></li>
  </ul>
</ol>

<hr>

<h3>Tech Stack</h3>
<ul>
  <li><strong>Language:</strong> Python 3.12</li>
  <li><strong>Libraries:</strong>
  <ul>
    <li><code>requests</code> - for API calls</li>
    <li><code>boto3</code> - for AWS S3 connection </li>
    <li><code>python-dotenv</code> - for secret management</li>
  </ul>
  <li><strong>Logging:</strong> Dual-stream file logging for both Extract and Load phases.</li>
  <li><strong>Cloud Services:</strong> AWS S3, Snowflake, dbt Platform</li>
</ul>

<hr />

<h2>📂 Project Structure</h2>

<pre>
├── logs/                   
│   ├── extract/            # Timestamped logs for API extraction
│   └── load/               # Timestamped logs for S3 upload activity
├── modules/                
│   ├── extract.py          # Logic for TfL API interaction & retries
│   └── load.py             # Logic for AWS S3 authentication & file transfer
├── extracted_data/         # Temporary staging for raw .json files
├── .env                    # Environment variables (Hidden/Secret)
├── main.py                 # Primary entry point & pipeline orchestrator
├── requirements.txt        # Project dependencies
└── README.md
</pre>

<hr />

<h2>🛠️ Setup & Installation</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/bikepoint-pipeline.git
cd bikepoint-pipeline</code></pre>

<h3>2. Install Dependencies</h3>
<p>Ensure you have Python installed, then install the required packages:</p>
<pre><code>pip install requests boto3 python-dotenv</code></pre>

<h3>3. Configure Environment Variables</h3>
<p>Create a <code>.env</code> file in the root directory to store your AWS credentials securely. This project uses <code>python-dotenv</code> to load these secrets.</p>

<p><strong>File: <code>.env</code></strong></p>
<pre><code>AWS_ACCESS_KEY=your_access_key_here
AWS_SECRET_KEY=your_secret_key_here
AWS_BUCKET_NAME=your_s3_bucket_name</code></pre>

<hr />

<h2>🏃 Usage</h2>

<p>The entire pipeline is automated via the orchestrator script. Simply run:</p>

<pre><code>python main.py</code></pre>

<h3>Pipeline Features:</h3>
<ul>
  <li><strong>Resilience:</strong> The <code>extract</code> module includes a retry loop that waits 10 seconds between attempts for 500-level errors.</li>
  <li><strong>Atomic Uploads:</strong> The <code>load</code> module ensures files are only removed from the <code>extracted_data</code> folder once S3 confirms a successful write.</li>
  <li><strong>Granular Logging:</strong> Each run generates distinct log files in <code>logs/extract/</code> and <code>logs/load/</code> named with the execution timestamp for easy auditing.</li>
  <li><strong>Validation:</strong> The loader automatically filters for files, ensuring no system directories are accidentally uploaded to your S3 bucket.</li>
</ul>

<hr />

<h2>⚙️ Orchestration & Deployment</h2>

<p>
  This project is designed to be fully containerized and orchestrated for automated scheduling and monitoring. 
</p>

<ul>
  <li><strong>Containerization:</strong> The pipeline is compatible with <strong>Docker</strong>, ensuring a consistent environment for extraction and loading tasks across different infrastructure.</li>
  <li><strong>Workflow Management:</strong> The repository supports orchestration via <strong>Kestra</strong>. This allows for visual flow management, automated execution retries, and real-time alerting.</li>
  <li><strong>🔒 Security Note:</strong> To maintain project security, all <code>docker-compose.yml</code>, <code>.env</code>, and database configuration files have been added to <code>.gitignore</code>. This prevents the exposure of sensitive API keys, cloud credentials, and internal networking logic. </li>
</ul>

<hr />

<h2>📄 License</h2>
<p>This project is open source and available under the <a href="LICENSE">MIT License</a>.</p>
