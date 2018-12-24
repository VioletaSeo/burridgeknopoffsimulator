#pragma once

#include "odesolver/c/odesolver.h"


namespace odesolver {

class Euler : public OdeSolver
{
public:
    using OdeSolver::OdeSolver;

private:
    void step_impl() override;
};

}  // namespace odesolver
