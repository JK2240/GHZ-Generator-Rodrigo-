{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMCNhei5sdbgrKK5kYf/aSB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JK2240/GHZ-Generator-Rodrigo-/blob/main/B92_qkd.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "N1SWpHCb3kxG",
        "outputId": "cc6412f6-1472-4aec-edaf-1f5aacf74df7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting cirq\n",
            "  Downloading cirq-1.7.0-py3-none-any.whl.metadata (15 kB)\n",
            "Collecting cirq-google\n",
            "  Downloading cirq_google-1.7.0-py3-none-any.whl.metadata (4.8 kB)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (2.0.2)\n",
            "Collecting numpy\n",
            "  Downloading numpy-2.5.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)\n",
            "Collecting cirq-aqt==1.7.0 (from cirq)\n",
            "  Downloading cirq_aqt-1.7.0-py3-none-any.whl.metadata (4.7 kB)\n",
            "Collecting cirq-core==1.7.0 (from cirq)\n",
            "  Downloading cirq_core-1.7.0-py3-none-any.whl.metadata (4.8 kB)\n",
            "Collecting cirq-ionq==1.7.0 (from cirq)\n",
            "  Downloading cirq_ionq-1.7.0-py3-none-any.whl.metadata (4.7 kB)\n",
            "Collecting cirq-pasqal==1.7.0 (from cirq)\n",
            "  Downloading cirq_pasqal-1.7.0-py3-none-any.whl.metadata (4.7 kB)\n",
            "Collecting cirq-web==1.7.0 (from cirq)\n",
            "  Downloading cirq_web-1.7.0-py3-none-any.whl.metadata (5.4 kB)\n",
            "Requirement already satisfied: google-api-core~=2.24 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]~=2.24->cirq-google) (2.30.3)\n",
            "Requirement already satisfied: proto-plus~=1.25 in /usr/local/lib/python3.12/dist-packages (from cirq-google) (1.28.1)\n",
            "Collecting protobuf<7.0dev,>=6.32.1 (from cirq-google)\n",
            "  Downloading protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl.metadata (593 bytes)\n",
            "Collecting typedunits (from cirq-google)\n",
            "  Downloading typedunits-0.0.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)\n",
            "Requirement already satisfied: requests~=2.32 in /usr/local/lib/python3.12/dist-packages (from cirq-aqt==1.7.0->cirq) (2.32.4)\n",
            "Requirement already satisfied: attrs>=21.3.0 in /usr/local/lib/python3.12/dist-packages (from cirq-core==1.7.0->cirq) (26.1.0)\n",
            "Collecting duet>=0.2.8 (from cirq-core==1.7.0->cirq)\n",
            "  Downloading duet-0.2.9-py3-none-any.whl.metadata (2.3 kB)\n",
            "Requirement already satisfied: matplotlib~=3.9 in /usr/local/lib/python3.12/dist-packages (from cirq-core==1.7.0->cirq) (3.10.0)\n",
            "Requirement already satisfied: networkx~=3.4 in /usr/local/lib/python3.12/dist-packages (from cirq-core==1.7.0->cirq) (3.6.1)\n",
            "Collecting pandas<3.1.0.dev,>=2.3 (from cirq-core==1.7.0->cirq)\n",
            "  Downloading pandas-3.0.5-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.5/79.5 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: scipy~=1.15 in /usr/local/lib/python3.12/dist-packages (from cirq-core==1.7.0->cirq) (1.16.3)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.12/dist-packages (from cirq-core==1.7.0->cirq) (1.14.0)\n",
            "Requirement already satisfied: tqdm>=4.12 in /usr/local/lib/python3.12/dist-packages (from cirq-core==1.7.0->cirq) (4.67.3)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.63.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (1.75.0)\n",
            "Requirement already satisfied: google-auth<3.0.0,>=2.14.1 in /usr/local/lib/python3.12/dist-packages (from google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (2.49.0)\n",
            "Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]~=2.24->cirq-google) (1.82.1)\n",
            "Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]~=2.24->cirq-google) (1.71.2)\n",
            "Requirement already satisfied: cython>=3.0.0 in /usr/local/lib/python3.12/dist-packages (from typedunits->cirq-google) (3.0.12)\n",
            "Requirement already satisfied: pyparsing in /usr/local/lib/python3.12/dist-packages (from typedunits->cirq-google) (3.3.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.12/dist-packages (from google-auth<3.0.0,>=2.14.1->google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (0.4.2)\n",
            "Requirement already satisfied: cryptography>=38.0.3 in /usr/local/lib/python3.12/dist-packages (from google-auth<3.0.0,>=2.14.1->google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (49.0.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.12/dist-packages (from google-auth<3.0.0,>=2.14.1->google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (4.9.1)\n",
            "Requirement already satisfied: typing-extensions~=4.12 in /usr/local/lib/python3.12/dist-packages (from grpcio<2.0.0,>=1.33.2->google-api-core[grpc]~=2.24->cirq-google) (4.16.0)\n",
            "INFO: pip is looking at multiple versions of grpcio-status to determine which version is compatible with other requirements. This could take a while.\n",
            "Collecting grpcio-status<2.0.0,>=1.33.2 (from google-api-core[grpc]~=2.24->cirq-google)\n",
            "  Downloading grpcio_status-1.83.0-py3-none-any.whl.metadata (1.2 kB)\n",
            "Collecting grpcio<2.0.0,>=1.33.2 (from google-api-core[grpc]~=2.24->cirq-google)\n",
            "  Downloading grpcio-1.83.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (3.7 kB)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib~=3.9->cirq-core==1.7.0->cirq) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib~=3.9->cirq-core==1.7.0->cirq) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib~=3.9->cirq-core==1.7.0->cirq) (4.63.0)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib~=3.9->cirq-core==1.7.0->cirq) (1.5.0)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib~=3.9->cirq-core==1.7.0->cirq) (26.2)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib~=3.9->cirq-core==1.7.0->cirq) (11.3.0)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.12/dist-packages (from matplotlib~=3.9->cirq-core==1.7.0->cirq) (2.9.0.post0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests~=2.32->cirq-aqt==1.7.0->cirq) (3.4.9)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests~=2.32->cirq-aqt==1.7.0->cirq) (3.18)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests~=2.32->cirq-aqt==1.7.0->cirq) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests~=2.32->cirq-aqt==1.7.0->cirq) (2026.6.17)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from sympy->cirq-core==1.7.0->cirq) (1.3.0)\n",
            "Requirement already satisfied: cffi>=2.0.0 in /usr/local/lib/python3.12/dist-packages (from cryptography>=38.0.3->google-auth<3.0.0,>=2.14.1->google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (2.1.0)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in /usr/local/lib/python3.12/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.14.1->google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (0.6.4)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.7->matplotlib~=3.9->cirq-core==1.7.0->cirq) (1.17.0)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.12/dist-packages (from cffi>=2.0.0->cryptography>=38.0.3->google-auth<3.0.0,>=2.14.1->google-api-core~=2.24->google-api-core[grpc]~=2.24->cirq-google) (3.0)\n",
            "Downloading cirq-1.7.0-py3-none-any.whl (11 kB)\n",
            "Downloading cirq_google-1.7.0-py3-none-any.whl (733 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m733.7/733.7 kB\u001b[0m \u001b[31m17.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading cirq_aqt-1.7.0-py3-none-any.whl (32 kB)\n",
            "Downloading cirq_core-1.7.0-py3-none-any.whl (2.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.1/2.1 MB\u001b[0m \u001b[31m55.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading cirq_ionq-1.7.0-py3-none-any.whl (77 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m77.6/77.6 kB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading cirq_pasqal-1.7.0-py3-none-any.whl (34 kB)\n",
            "Downloading cirq_web-1.7.0-py3-none-any.whl (294 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m294.0/294.0 kB\u001b[0m \u001b[31m17.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading numpy-2.5.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m16.7/16.7 MB\u001b[0m \u001b[31m58.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl (323 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m323.4/323.4 kB\u001b[0m \u001b[31m20.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading typedunits-0.0.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (2.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.7/2.7 MB\u001b[0m \u001b[31m70.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading duet-0.2.9-py3-none-any.whl (29 kB)\n",
            "Downloading grpcio_status-1.83.0-py3-none-any.whl (14 kB)\n",
            "Downloading grpcio-1.83.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (7.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m7.0/7.0 MB\u001b[0m \u001b[31m77.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pandas-3.0.5-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (11.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.0/11.0 MB\u001b[0m \u001b[31m68.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: protobuf, numpy, grpcio, duet, typedunits, pandas, grpcio-status, cirq-core, cirq-web, cirq-pasqal, cirq-ionq, cirq-aqt, cirq-google, cirq\n",
            "  Attempting uninstall: protobuf\n",
            "    Found existing installation: protobuf 5.29.6\n",
            "    Uninstalling protobuf-5.29.6:\n",
            "      Successfully uninstalled protobuf-5.29.6\n",
            "  Attempting uninstall: numpy\n",
            "    Found existing installation: numpy 2.0.2\n",
            "    Uninstalling numpy-2.0.2:\n",
            "      Successfully uninstalled numpy-2.0.2\n",
            "  Attempting uninstall: grpcio\n",
            "    Found existing installation: grpcio 1.82.1\n",
            "    Uninstalling grpcio-1.82.1:\n",
            "      Successfully uninstalled grpcio-1.82.1\n",
            "  Attempting uninstall: pandas\n",
            "    Found existing installation: pandas 2.2.2\n",
            "    Uninstalling pandas-2.2.2:\n",
            "      Successfully uninstalled pandas-2.2.2\n",
            "  Attempting uninstall: grpcio-status\n",
            "    Found existing installation: grpcio-status 1.71.2\n",
            "    Uninstalling grpcio-status-1.71.2:\n",
            "      Successfully uninstalled grpcio-status-1.71.2\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-colab 1.0.0 requires pandas==2.2.2, but you have pandas 3.0.5 which is incompatible.\n",
            "google-ai-generativelanguage 0.6.15 requires protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.2, but you have protobuf 6.33.6 which is incompatible.\n",
            "numba 0.60.0 requires numpy<2.1,>=1.22, but you have numpy 2.5.1 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed cirq-1.7.0 cirq-aqt-1.7.0 cirq-core-1.7.0 cirq-google-1.7.0 cirq-ionq-1.7.0 cirq-pasqal-1.7.0 cirq-web-1.7.0 duet-0.2.9 grpcio-1.83.0 grpcio-status-1.83.0 numpy-2.5.1 pandas-3.0.5 protobuf-6.33.6 typedunits-0.0.2\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "google",
                  "numpy"
                ]
              },
              "id": "86ec551f0ae0489aa91be7a2be13229d"
            }
          },
          "metadata": {}
        }
      ],
      "source": [
        "!pip install --upgrade cirq cirq-google numpy"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  import cirq\n",
        "except ImportError:\n",
        "  print (\"installing cirq...\")\n",
        "  !pip install --quiet cirq\n",
        "  print(\"installed cirq.\")\n",
        "  import cirq\n",
        "\n",
        "import cirq_google\n",
        "import cirq_web\n",
        "import numpy as np\n",
        "import math\n",
        "import scipy\n",
        "import sympy\n",
        "import random\n",
        "import matplotlib.pyplot as plt\n",
        "import sys\n",
        "sys.meta_path[:] = [f for f in sys.meta_path if \"DaskFinder\" not in str(f)]\n",
        "from math import radians, degrees\n",
        "from scipy.optimize import minimize\n",
        "from cirq_web import bloch_sphere\n",
        "from cirq import Z, PauliSum\n",
        "\n",
        "import sys\n",
        "sys.meta_path[:] = [f for f in sys.meta_path if \"DaskFinder\" not in str(f)]"
      ],
      "metadata": {
        "id": "HIB0pgjy3nth"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def run_B92(repetitions):\n",
        "  alice_key = []\n",
        "  bob_key = []\n",
        "  my_qubits = []\n",
        "  for i in range (repetitions):\n",
        "    q = cirq.NamedQubit(\"q\")\n",
        "    simulator = cirq.Simulator()\n",
        "\n",
        "    alice_bit = random.choice([0, 1])\n",
        "\n",
        "    circuit = cirq.Circuit()\n",
        "    if alice_bit == 1:\n",
        "      circuit.append(cirq.X(q))\n",
        "      circuit.append(cirq.H(q))\n",
        "\n",
        "    bob_basis = random.choice(['Z', 'X'])\n",
        "\n",
        "    if bob_basis == 'X' and alice_bit == 0:\n",
        "        circuit.append(cirq.measure(q, key='mm'))\n",
        "        result = simulator.run(circuit, repetitions=1)\n",
        "        measurement = result.measurements['mm'][0][0]\n",
        "        if measurement == 0:\n",
        "          alice_key.append(alice_bit)\n",
        "          bob_key.append(measurement)\n",
        "\n",
        "         # print(circuit)\n",
        "         # print(result)\n",
        "          my_qubits.append(result)\n",
        "          #print(f\"Alice's Secret Bit: {alice_bit}\")\n",
        "          #print(f\"Bob's Chosen Basis: {bob_basis}, measured {measurement}\")\n",
        "          #print(\"-\" * 30)\n",
        "\n",
        "    elif bob_basis == 'Z' and alice_bit == 1:\n",
        "        circuit.append(cirq.H(q))\n",
        "        circuit.append(cirq.measure(q, key = 'mm'))\n",
        "        result = simulator.run(circuit, repetitions=1)\n",
        "        measurement = result.measurements['mm'][0][0]\n",
        "        if measurement == 1:\n",
        "          alice_key.append(alice_bit)\n",
        "          bob_key.append(measurement)\n",
        "\n",
        "          #print(circuit)\n",
        "          #print(result)\n",
        "          my_qubits.append(result)\n",
        "          #print(f\"Alice's Secret Bit: {alice_bit}\")\n",
        "          #print(f\"Bob's Chosen Basis: {bob_basis}, measured {measurement}\")\n",
        "          #print(\"-\" * 30)\n",
        "    #else:\n",
        "          #print(\"Discard\")\n",
        "          #print(\"-\" * 30)\n",
        "\n",
        "    # Display results and verify security\n",
        "    #print(\"\\n--- Final Results ---\")\n",
        "    #print(f\"Alice's Key:   {alice_key}\")\n",
        "    #print(f\"Bob's Key:     {bob_key}\")\n",
        "\n",
        "    # Check if keys match perfectly\n",
        "    if alice_key == bob_key:\n",
        "        #print(\"[+] SUCCESS: All keys match perfectly! Channel is secure.\")\n",
        "        shared_key = [int(key) for key in alice_key]\n",
        "        #print(f\"Shared Key: {shared_key}\")\n",
        "\n",
        "  print(shared_key)\n",
        "  return shared_key"
      ],
      "metadata": {
        "id": "l-UCg5nztSpG"
      },
      "execution_count": 149,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sharedkey = run_B92(30)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-d0UcKmvt0WG",
        "outputId": "fd6ec5c4-47a9-46a6-a96a-478168a6fcb0"
      },
      "execution_count": 150,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]\n"
          ]
        }
      ]
    }
  ]
}