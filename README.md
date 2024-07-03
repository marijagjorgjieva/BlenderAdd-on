# Data visualization Blender add-on 

*TODO:*

## Default features
- Scatterplot
- Barchart
- Histplot
- Linechart
- Axis with labels

### User Interaction and Customization
Provide customizable panels where users can select different visualization options and tweak parameters.
  
## NLP features
### Visualizing n-grams histplot
### Topic Modeling Visualization 
- Generate 3D word clouds for each topic, with word size representing the frequency or importance of words.
### Text Embedding Visualization
- 2D/3D Scatter Plots- Visualize high-dimensional text embeddings (e.g., word2vec, BERT) to project them into 2D or 3D space.
- Clustering- Show clusters of similar words or documents, highlighting how different texts or words group together based on their semantic similarities.

*DONE:*
- simple csv import operator `ImportCSVOperator` which allows importing CSV data to create 3D shapes based on specified coordinates and properties. [link](https://github.com/marijagjorgjieva/BlenderAddon/blob/main/import_csv_operator.py)
- `ApplyChangesOperator` which allows adjusting size and color, and applying these settings to imported objects. [link](https://github.com/marijagjorgjieva/BlenderAddon/blob/main/apply_changes_operator.py)
- `CSVImporterPanel` displays UI elements for interacting with CSV import functionality [link](https://github.com/marijagjorgjieva/BlenderAddon/blob/main/csv_importer_panel.py)

