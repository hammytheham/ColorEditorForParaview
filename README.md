# ColorEditorForParaview
I wanted to fine tune my Paraview B&amp;W preset scheme to increase the resolution in certain areas of my data range but the 'Color transfer values' dialog box is pretty crap for this purpose. Or perhaps there is a way in Paraview and I'm just being dumb? Anyway this is a very simple (rather scruffy) python code that edits a json preset scheme that someone out there may find useful!
To use:
1. Clone the Git
2. Open the ColorMapEditor.py, edit the VarA,VarB etc section and including the new path to the template BlankBW.json file and your new output Preset name.  
3. Run the python script.
4. In paraview Go to: Color Map Editor> Choose Preset > Import > YourNewPreset

