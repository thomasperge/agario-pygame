# 🎮 Agario-Pygame

AgarioPygame is a Python adaptation with Pygame of the game agar.io. Players can choose between keyboard and mouse controls, select their difficulty level, and must avoid traps while maintaining their size to achieve the highest score.

## ➡️ How to play ? - Requirements
```bash
- Python (version utilisée pour le développement : 3.11.7)
- Pygame (version : 2.5.2)
- Pip (version : 23.3.1)
```

## ➡️ Installation

Clone the project :

```bash
git clone https://github.com/B2-Info-23-24/agarpyo-b2-a-thomasperge.git
```

Go to project folder :

```bash
cd agarpyo-b2-a-thomasperge
```

Create and paste environment.yml into the project's root directory
```bash
name: agario-pygame
channels:
  - defaults
dependencies:
  - bzip2=1.0.8=he774522_0
  - ca-certificates=2023.12.12=haa95532_0
  - libffi=3.4.4=hd77b12b_0
  - openssl=3.0.13=h2bbff1b_0
  - pip=23.3.1=py311haa95532_0
  - python=3.11.7=he1021f5_0
  - setuptools=68.2.2=py311haa95532_0
  - sqlite=3.41.2=h2bbff1b_0
  - tk=8.6.12=h2bbff1b_0
  - tzdata=2023d=h04d1e81_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wheel=0.41.2=py311haa95532_0
  - xz=5.4.5=h8cc25b3_0
  - zlib=1.2.13=h8cc25b3_0
  - pip:
      - pygame==2.5.2
```

Create and activate a virtual environment from an environement.yml import file
```bash
conda env create -f environment.yaml
conda activate agario-pygame
```

Run the project

```bash
python main.py
```

## ➡️ Utilisation
#### Menu
In the menu, you have the option to choose between playing with the keyboard and mouse, as well as adjusting the game difficulty

![App Screenshot](https://cdn.discordapp.com/attachments/1086733730586038352/1206271887966076978/image.png?ex=65db673d&is=65c8f23d&hm=bea8a8bbfd02d423e9b30bef366cbd8d62aea42c7ee647f99d7a4a8121416a92&)

#### Game
In the game, you have traps and feeds. Once you eat a feed (green ball), your speed and size increase. If you hit a trap (red ball) and your size is larger than the trap, your size decreases by half, and so does your speed

![App Screenshot](https://cdn.discordapp.com/attachments/1086733730586038352/1206272088818585660/image.png?ex=65db676d&is=65c8f26d&hm=2776f647c31b086bbb9afcb3b4b185ec472354a6fd17dacbab745b81be0bfc24&)

#### Score
When the timer runs out, you have a small screen showing your final score

![App Screenshot](https://cdn.discordapp.com/attachments/1086733730586038352/1206272285577838613/image.png?ex=65db679c&is=65c8f29c&hm=c6caf5e60921c59efee4571b0590413858ae4fdf1cbf568a16be483e8fc70e28&)


## ➡️ License

This project is under the [MIT](https://choosealicense.com/licenses/mit/) license

