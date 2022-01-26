#include "mcs-dl-env.h"

namespace ns3 {

MCSDL::MCSDL (uint16_t id) : Ns3AIDL<mcsFeature, mcsPredicted, mcsTarget> (id)

{
    SetCond(2,0);
}

void
MCSDL::SetSINR(double sinr)
{
    auto feature = FeatureSetterCond();
    feature->sinr = sinr;
    SetCompleted();
}

void
MCSDL::SetTarget (uint8_t tar)
{
    auto target = TargetSetterCond();
    target->target = tar;
    SetCompleted();
}

uint32_t
MCSDL::GetMCS (void)
{
    auto pred = PredictedGetterCond();
    uint32_t index = pred->new_MCS;
    GetCompleted();
    return index;
}

uint8_t
MCSDL::GetTarget(void)
{
    auto tar = TargetGetterCond();
    uint8_t ret = tar->target;
    GetCompleted();
    return ret;
}

}
