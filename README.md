<img title="a title" alt="Alt text" src="images/logo_frameworkfusion_ai.svg">

# FrameworkFusion

FrameworkFusion is a tool designed to leverage the [OpenCRE Library](https://github.com/cristianovisk/opencre_lib) to correlate and visualize relationships between security frameworks mapped in the [OpenCRE](https://www.opencre.org/) database. It aims to simplify the task of understanding compliance overlaps and aligning security controls across multiple frameworks.

## 📚 Features

- Correlate controls across different security frameworks.
- Generate and visualize mapping tables for frameworks.
- Easy-to-use interface for querying relationships.
- Built on top of the powerful [OpenCRE Library](https://github.com/cristianovisk/opencre_lib).

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.8 or higher installed.

### Installation

1. Install using PIP:
   ```bash
   pip3 install frameworkfusion

2. How use:
    ```bash
    framework_fusion compare --primary 12 --secundary 4 --output compare.xlsx

3. To see frameworks supported:
    ```bash
    framework_fusion example