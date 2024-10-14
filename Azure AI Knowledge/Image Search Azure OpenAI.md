Connect blob storage where images are present

Set up text embedding model to convert input text to embeddings

Vectorize and enrich images:
- Use Azure AI vision to generate vector representation of the image files
- The Wizard also uses OCR to recognize text in image files
	- Two more fields are generated
		- `chunk`the OCR generated string of any text found in the image
		- `text_vector`embedding that represents the `chunk` string

Specify a run time schedule for the indexer.

The Image Search OpenAI Wizard creates the following: 
1. Indexer
2. Data source connection
3. index with vector fields, text fields
4. Vectorizers
5. Vector algorithms

It uses a skillset with the following 5 skills:
- OCR Skill - Recognizes text in image files
- Text Merger Skill - Unifies various outputs of OCR processing
- Text Split Skill - Adds data chunking
- Azure AI Vision Multimodal - Used to vectorize text generated from OCR
- Azure AI Vision Multimodal - Used to vectorize images

### OCR Cognitive Skill

Recognizes printed and handwritten text in image files.

Uses the ML models provided by the Azure AI Vision API.

The OCR skill extracts text from image files.. JPEG, JPG, PNG, BMP and TIFF

Can detect text orientation, language of the text and text separators..

Takes in an image input generated from the Azure blob indexer

Outputs: 
- text
- layout Information of the image in the text
If you call OCR on images embeded in PDFs, OCR output will be located at the bottom of the page after any text that was extracted and processed. 

### Azure AI Vision Multimodal

Uses the  Azure AI Vision's [multimodal embeddings API](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-image-retrieval) to generate embeddings for image or text input.

This outputs an embedding array of floats for the input text or image.

#### Azure Multimodal Embeddings

Enable vectorization of images and text queries. Convert images to coordinates in a n-dimensional vector space. 

Similarly incoming queries can also be converted to vectors, and both these can be matched in the n-dimensional space based on semantic closeness..

This allows user to search for a set of images using text without the need to use image tags or other meta data. 

Related project - Skin Rash Visualization using Latent Diffusion Models with Clip


### Business Applications:
- Digital asset management - search for image or a video in gallery based on visual features
- Security and surveillance - Search for images based on specific features or patterns
- Medical and Forensic Image retrieval
- E commerce
- Fashion and Design

Link to your project on building a diffusion model pipeline to generate Rash Based images using text based input.. And talk about some of the challenges I faced.

![Diagram of the multimodal embedding / image retrieval process.](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/media/image-retrieval.png)