#include "ns3/ns3-ai-dl.h"

namespace ns3 {

struct mcsFeature
{
    double sinr;
};

struct mcsPredicted
{
    uint32_t new_MCS;
};

struct mcsTarget
{
    uint8_t target;
};

class MCSDL : public Ns3AIDL<mcsFeature, mcsPredicted, mcsTarget>
{
public:
    MCSDL (void) = delete;
    MCSDL (uint16_t);
    void SetSINR(double sinr);
    void SetTarget(uint8_t tar);
    
    uint32_t GetMCS(void);
    uint8_t GetTarget(void);
};

}