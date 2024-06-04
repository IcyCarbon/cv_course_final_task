# CV Course Final Task: Man-vehicle Monitoring Task for Tower Security Monitoring  

## 1 Task Description

This course systematically introduces the basic principles, typical methods & cutting-edge practical technologies of computer vision (CV). To improve students' in-depth understanding for the latest methods & technologies of CV, this assessment aims to develop a CV-based algorithm for a cutting-edge application. A report should be summarized and submitted finally. (Note: It is encouraged to form an innovative work based on the achievements published from CV-related Top journal/conferences in the past three years (the assessment results are directly excellent).)



The purpose of this task is to combine the cutting-edge technologies in the field of computer vision to carry out high-precision human-vehicle detection under the top-down view for the images captured at the high and medium positions of the pylons. Through teamwork, students will learn skills such as analyzing experimental results, adjusting model hyperparameters, optimizing network structure, etc., to improve teamwork and practical ability.

## 2 Task Requirements

- Team Formation: 2 students per group.

- Counting program design and code development: students are required to complete the design of the human-vehicle detection program and complete the code development in conjunction with the existing topical/topical conference results.

- Analysis of Experimental Results: Students need to analyze the performance of the model in different scenarios and propose improvement strategies.

- Adjusting model hyperparameters: students need to try different model hyperparameters to improve the accuracy of human-vehicle detection.

- Network structure optimization: students can optimize the existing computer vision network structure according to the experimental results to improve the model performance, mainly including accuracy and real-time performance.

- Target Annotation: Students need to generate annotation files in Pascal VOC format to meet the requirements of model training.

- Summary of Work and Report Writing.

## 3 Dataset Description

This task provides 500 image data and labeled files from multiple day/night roadway pedestrian and vehicle scenes.

- Division of Training and Testing Sets: It is recommended to divide the training set and testing set in an 8:2 ratio while ensuring the randomness and representativeness of the data to ensure the model's generalization ability in real scenarios.

- Annotation Instructions: Annotation files must conform to the Pascal VOC format.

- File Description in the Compression Package

├──dataset：

​       ├── Annotations:  All images (500)

​       └── JPEGImages:  All annotated documents (500)

## 4 Task Submission( TO DO )

- - [ ] Experiment Report (including charts)：

> - [ ] Based on one task above, summarize its basic concepts, principles, framework, etc. (Chapter 1)

> - [ ] Related work (including itemized summary, the analysis of limitations, etc.) (Chapter 2)

> - [ ] The proposed method from this achievement (including clear logic line, pictures, tables, detailed flow charts/pseudocode, etc.) (Chapter 3, main part)

> - [ ] Analysis on training datasets (including collection approach, type, annotation method, etc.), and provide the cases based on different challenging factors (Chapter 4)

> - [ ] Qualitative and quantitative evaluation for the proposed method on provided image or video datasets/benchmarks (Chapter 5)

> - [ ] Summary and future work (including your own opinions and analysis) (Chapter 6)

> References

- - [ ] Annotation Files: Image training set with annotation files containing ground truth.

## 5 Grading Criteria

🚀 Extensiveness and comprehensiveness of topic research.

🚩 Depth and logic of paper analysis.

✨ Depth and accuracy of experimental design and result evaluation.

📈 Improvement in model performance.

📋 Completeness and accuracy of annotation files.

✔️ Experimental indicators: The mandate will be assessed with two indicators:

- Average Precision (AP): a measure of the model's detection accuracy, needed to ensure that the detection results match the real target as closely as possible.

- Frames Per Second (FPS): a measure of how fast the model can process images, requiring the highest possible frame rate while maintaining accuracy.