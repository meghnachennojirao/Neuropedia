from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Neuron structure data
neuron_structure= {
  "Cell Body (Soma)": [
    {
      "scientist": "Santiago Ramón y Cajal",
      "contribution": "Laid the foundation for understanding neuron anatomy"
    },
    {
      "scientist": "Camillo Golgi",
      "contribution": "Developed the Golgi stain for visualizing neuron structure"
    }
  ],
  "Dendrites": [
    {
      "scientist": "Wilhelm His, Sr.",
      "contribution": "Described the presence of dendrites in neurons"
    },
    {
      "scientist": "Rodolfo Llinás",
      "contribution": "Studied electrophysiological properties of dendrites"
    }
  ],
  "Axon": [
    {
      "scientist": "Hermann von Helmholtz",
      "contribution": "Demonstrated transmission speed along axons"
    },
    {
      "scientist": "Alan Hodgkin and Andrew Huxley",
      "contribution": "Developed the Hodgkin-Huxley model explaining action potential"
    }
  ],
  "Myelin Sheath": [
    {
      "scientist": "Rudolf Virchow",
      "contribution": "Coined the term 'myelin'"
    },
    {
      "scientist": "Camillo Golgi",
      "contribution": "Identified myelin sheath around axons"
    },
    {
      "scientist": "Marie Remy Bunge",
      "contribution": "Researched Schwann cells in myelination"
    }
  ],
  "Nodes of Ranvier": [
    {
      "scientist": "Louis-Antoine Ranvier",
      "contribution": "Discovered nodes of Ranvier"
    },
    {
      "scientist": "K.S. Cole",
      "contribution": "Contributed to understanding electrical properties"
    }
  ],
  "Synapse": [
    {
      "scientist": "Charles Scott Sherrington",
      "contribution": "Coined the term 'synapse'"
    },
    {
      "scientist": "Otto Loewi",
      "contribution": "Discovered chemical nature of synaptic transmission"
    }
  ],
  "Neurotransmitters": [
    {
      "scientist": "Henry Dale",
      "contribution": "Discovered acetylcholine"
    },
    {
      "scientist": "Arvid Carlsson",
      "contribution": "Discovered dopamine's role as a neurotransmitter"
    }
  ],
  "Neuroglia (Glial Cells)": [
    {
      "scientist": "Rudolf Virchow",
      "contribution": "Coined the term 'neuroglia'"
    },
    {
      "scientist": "Pío del Río Hortega",
      "contribution": "Identified microglia and oligodendrocytes"
    }
  ],
  "Synaptic Vesicles": [
    {
      "scientist": "Paul Greengard",
      "contribution": "Contributed to understanding synaptic transmission mechanisms"
    },
    {
      "scientist": "James Rothman and Randy Schekman",
      "contribution": "Awarded Nobel Prize for discoveries in vesicle trafficking"
    }
  ],
  "Ion Channels": [
    {
      "scientist": "Erwin Neher and Bert Sakmann",
      "contribution": "Developed the patch-clamp technique"
    }
  ],
  "Additional Contributions": [
    {
      "scientist": "Eric Kandel",
      "contribution": "Studied molecular mechanisms of learning and memory"
    },
    {
      "scientist": "John Eccles",
      "contribution": "Conducted pioneering work on synaptic mechanisms"
    }
  ]
}

@app.route('/api/data', methods=['GET'])
def get_data():
    search_query = request.args.get('search', '').lower()  # Get search query parameter and convert to lowercase
    filtered_data = {part: scientists for part, scientists in neuron_structure.items() if search_query in part.lower()}
    return jsonify(filtered_data)


if __name__ == '__main__':
    app.run(debug=True)
