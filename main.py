import json
import os
from fpdf import FPDF
from datetime import datetime, timedelta


class Estimate:

    def __init__(self, client_name, job_type, project_size, materials_needed,
                 complexity_level, additional_notes):
        self.client_name = client_name
        self.job_type = job_type
        self.project_size = project_size
        self.materials_needed = materials_needed
        self.complexity_level = complexity_level
        self.additional_notes = additional_notes
        self.estimated_hours = 0
        self.labor_cost = 0
        self.material_cost = 0
        self.total_cost = 0
        self.multi_stage_surcharge = 50 if complexity_level > 1 else 0
        self.expiration_date = datetime.now() + timedelta(days=7)

    def calculate_estimate(self):
        # Simplified calculation logic for demonstration
        self.estimated_hours = self.project_size * self.complexity_level
        self.labor_cost = self.estimated_hours * 80
        self.material_cost = self.project_size * 20  # Simplified material cost calculation
        self.total_cost = self.labor_cost + self.material_cost + self.multi_stage_surcharge

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="HTG Pro Services Estimate", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Client Name: {self.client_name}", ln=True)
        pdf.cell(200, 10, txt=f"Job Type: {self.job_type}", ln=True)
        pdf.cell(200,
                 10,
                 txt=f"Estimated Hours: {self.estimated_hours}",
                 ln=True)
        pdf.cell(200, 10, txt=f"Labor Cost: ${self.labor_cost}", ln=True)
        pdf.cell(200, 10, txt=f"Material Cost: ${self.material_cost}", ln=True)
        pdf.cell(200, 10, txt=f"Total Cost: ${self.total_cost}", ln=True)
        pdf.cell(
            200,
            10,
            txt=f"Expiration Date: {self.expiration_date.strftime('%Y-%m-%d')}",
            ln=True)
        pdf.output(f"{self.client_name}_estimate.pdf")

    def save_to_json(self):
        estimate_data = {
            "client_name": self.client_name,
            "job_type": self.job_type,
            "project_size": self.project_size,
            "materials_needed": self.materials_needed,
            "complexity_level": self.complexity_level,
            "additional_notes": self.additional_notes,
            "estimated_hours": self.estimated_hours,
            "labor_cost": self.labor_cost,
            "material_cost": self.material_cost,
            "total_cost": self.total_cost,
            "multi_stage_surcharge": self.multi_stage_surcharge,
            "expiration_date": self.expiration_date.strftime('%Y-%m-%d')
        }
        with open(f"{self.client_name}_estimate.json", "w") as json_file:
            json.dump(estimate_data, json_file, indent=4)


# Example usage
if __name__ == "__main__":
    client_name = input("Enter client name: ")
    job_type = input("Enter job type: ")
    project_size = int(input("Enter project size (in square feet): "))
    materials_needed = input("Enter materials needed: ")
    complexity_level = int(input("Enter complexity level (1-5): "))
    additional_notes = input("Enter additional notes: ")

    estimate = Estimate(client_name, job_type, project_size, materials_needed,
                        complexity_level, additional_notes)
    estimate.calculate_estimate()
    estimate.generate_pdf()
    estimate.save_to_json()
    print(f"Estimate generated for {client_name}.")
