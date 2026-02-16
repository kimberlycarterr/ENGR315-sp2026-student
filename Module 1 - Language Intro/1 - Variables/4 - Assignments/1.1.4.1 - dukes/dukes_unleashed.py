"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
# tuition costs are from the 2023-2024 school year
in_state_cost = 30792 # cost of in state tuition
out_state_cost = 47882 # cost of out of state tuition
r = .05 # alumni investment return in decimal form

in_state_gift = in_state_cost/r # Formula to find the gift needed to pay for in state tuition
out_state_gift = out_state_cost/r # Formula to find the gift needed to pay for out of state tuition

print(f"The donation needed for the in state student is ${in_state_gift}")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
print(f"The donation needed for the out of state student is ${out_state_gift}")
=======
print(f"The donation needed for the in state student is ${out_state_gift}")
>>>>>>> Stashed changes
=======
print(f"The donation needed for the in state student is ${out_state_gift}")
>>>>>>> Stashed changes
