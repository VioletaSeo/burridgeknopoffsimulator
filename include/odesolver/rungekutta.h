#pragma once

#include <odesolver/odesolver.h>


class RungeKutta : public OdeSolver
{
public:
    virtual ~RungeKutta() = default;

protected:
    RungeKutta(const std::vector<double>& step_weights,
               const std::vector<double>& weight_coefficients,
               OdeSolver::FuncType difeqs);
private:
    void step_impl() override;

    std::vector<double> m_step_weights;
    std::vector<double> m_weight_coefficients;

    double m_total_weight;
};