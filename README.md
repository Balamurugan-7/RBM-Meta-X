<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meta-X</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #bbb 1px solid;
            margin-bottom: 20px;
        }
        header h1 {
            text-align: center;
            text-transform: uppercase;
            margin: 0;
        }
        h2 {
            color: #333;
        }
        code {
            background: #e1e1e1;
            padding: 2px 4px;
            border-radius: 3px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            padding: 10px;
            background: #fff;
            border: 1px solid #ddd;
            margin-bottom: 5px;
        }
        .footer {
            text-align: center;
            padding: 10px;
            background: #333;
            color: #fff;
            position: absolute;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Meta-X</h1>
        </div>
    </header>

    <div class="container">
        <h2>Introduction</h2>
        <p>Meta-X is a powerful tool designed for conducting meta-analyses with ease. It aggregates and analyzes data from multiple studies, providing comprehensive insights and facilitating evidence-based decision-making.</p>

        <h2>Features</h2>
        <ul>
            <li><strong>Automated Data Integration:</strong> Seamlessly combine data from various sources.</li>
            <li><strong>Advanced Statistical Methods:</strong> Utilize cutting-edge algorithms for accurate analysis.</li>
            <li><strong>Customizable Reports:</strong> Generate reports tailored to your needs.</li>
            <li><strong>User-Friendly Interface:</strong> Intuitive design for efficient operation.</li>
        </ul>

        <h2>Installation</h2>
        <ol>
            <li><strong>Clone the Repository:</strong> <code>git clone https://github.com/yourusername/meta-x.git</code></li>
            <li><strong>Navigate to the Directory:</strong> <code>cd meta-x</code></li>
            <li><strong>Install Dependencies:</strong> Ensure you have Python 3.8+ installed. Then run: <code>pip install -r requirements.txt</code></li>
            <li><strong>Run Meta-X:</strong> <code>python meta_x.py</code></li>
        </ol>

        <h2>Usage</h2>
        <ol>
            <li><strong>Prepare Your Data:</strong> Ensure your data is in the required format. Refer to the <code>data_format.md</code> file for detailed specifications.</li>
            <li><strong>Load Data:</strong> Use the Meta-X interface to upload your datasets.</li>
            <li><strong>Configure Analysis:</strong> Choose your analysis parameters through the settings menu.</li>
            <li><strong>Run Analysis:</strong> Start the analysis and wait for the results.</li>
            <li><strong>Review Reports:</strong> Access and review your customized reports from the output directory.</li>
        </ol>

        <h2>Configuration</h2>
        <p>Meta-X can be customized via the <code>config.yml</code> file. Adjust the settings to fit your specific requirements.</p>

        <h2>Contributing</h2>
        <p>We welcome contributions to Meta-X! If you have ideas for improvements or want to report issues, please submit a pull request or open an issue on our <a href="https://github.com/yourusername/meta-x/issues">GitHub repository</a>.</p>

        <h2>License</h2>
        <p>Meta-X is licensed under the <a href="LICENSE">MIT License</a>.</p>

        <h2>Contact</h2>
        <p>For questions or support, please reach out to us at <a href="mailto:support@meta-x.com">support@meta-x.com</a>.</p>
    </div>

    <footer class="footer">
        <p>&copy; 2024 Meta-X. All rights reserved.</p>
    </footer>
</body>
</html>
