import csv
from fpdf import FPDF

# Step 1: Read the data from a CSV file
def read_data(filename):
    data = []
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            data.append(row)
    return data

# Step 2: Analyze the data (simple analysis in this case)
def analyze_data(data):
    total_sales = 0
    count = len(data)
    
    for row in data:
        total_sales += float(row[1])  # Assuming the second column is sales data
    
    avg_sales = total_sales / count if count > 0 else 0
    return total_sales, avg_sales, count

# Step 3: Generate PDF Report
def generate_pdf_report(data, total_sales, avg_sales, count, output_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Set title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Sales Report", ln=True, align="C")
    
    # Add a summary
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total Sales: ${total_sales:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Average Sales: ${avg_sales:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Number of Entries: {count}", ln=True)
    
    # Add a table with the data
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80, 10, txt="Product", border=1, align="C")
    pdf.cell(50, 10, txt="Sales", border=1, align="C")
    pdf.ln()
    
    pdf.set_font('Arial', '', 12)
    for row in data:
        pdf.cell(80, 10, txt=row[0], border=1, align="C")  # Product name
        pdf.cell(50, 10, txt=row[1], border=1, align="C")  # Sales
        pdf.ln()
    
    # Output the PDF to a file
    pdf.output(output_filename)

# Main function to run the process
def main():
    input_file = 'sales_data.csv'  # Assuming your CSV file is named 'sales_data.csv'
    output_pdf = 'sales_report.pdf'
    
    data = read_data(input_file)
    total_sales, avg_sales, count = analyze_data(data)
    generate_pdf_report(data, total_sales, avg_sales, count, output_pdf)
    print(f"Report generated and saved as {output_pdf}")

if __name__ == "__main__":
    main()
