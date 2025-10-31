### boston-house price prediction

### Tools required

1. [render](https://render.com)
2. [Github Account](https://github.com)
3. [VSCodeIDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


### Setup steps  
```bash
git clone https://github.com/pratp-123/boston-housprice.git
cd boston-housprice
python3 -m venv venv         # or use conda
source venv/bin/activate     # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### libraries and tools
![Project Architecture](images/libraries.png)

![spread and skewness of each numerical feature](images/skewness.png)
You’ll see whether features like RM (rooms per dwelling) or LSTAT (lower status population %) are normally distributed or skewed.

![Relationship Between Key Features and Target](images/price%20vs%20feature.png)
✅ Insight:
RM increases with MEDV → more rooms, higher price
LSTAT decreases with MEDV → higher lower-status % = lower price

![scatter of predicted and actual data points](images/predected_scatter.png)

### Directory
```
Directory structure:
└── pratp-123-boston-housprice/
    ├── README.md
    ├── app.py
    ├── Dockerfile
    ├── LICENSE
    ├── Procfile
    ├── requirements.txt
    ├── scaling.pkl
    ├── templates/
    │   └── index.html
    └── .github/
        └── workflows/
            └── main.yaml
```
            



